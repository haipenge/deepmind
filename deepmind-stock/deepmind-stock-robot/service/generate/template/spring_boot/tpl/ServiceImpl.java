package ${obj.component.package_name()}.service.impl;

import java.util.Collection;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import org.apache.commons.collections.CollectionUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import ${obj.component.package_name()}.entity.${obj.name};
import ${obj.component.package_name()}.service.${obj.name}Service;
import ${obj.component.package_name()}.repository.${obj.project.repository}.${obj.name}Repository;
import com.faceye.feature.service.impl.BaseServiceImpl;

/**
 * @说明:${obj.name} 服务类<br>
 * @author @haipenge <br>
 * @联系:haipenge<br>
 * @Create Date:${obj.get_current_date()}<br>
 */
@Service
@Transactional
public class ${obj.name}ServiceImpl extends BaseServiceImpl<${obj.name}, Long, ${obj.name}Repository> implements ${obj.name}Service {

	@Autowired
	public ${obj.name}ServiceImpl(${obj.name}Repository dao) {
		super(dao);
	}
}